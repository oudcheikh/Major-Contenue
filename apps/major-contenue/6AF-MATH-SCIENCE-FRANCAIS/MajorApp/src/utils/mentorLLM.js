import { SYSTEM_PROMPT_GRAND_FRERE } from '../prompts/grandFrerePrompt';

let lastMentorError = '';

function setLastMentorError(msg) {
  lastMentorError = msg || '';
}

export function getLastMentorError() {
  return lastMentorError;
}

function cleanJsonString(raw) {
  if (!raw) return '';
  return raw.replace(/```json/gi, '').replace(/```/g, '').trim();
}

function parseSessionPayload(text) {
  try {
    const cleaned = cleanJsonString(text);
    let parsed = null;
    try {
      parsed = JSON.parse(cleaned);
    } catch {
      const start = cleaned.indexOf('{');
      const end = cleaned.lastIndexOf('}');
      if (start >= 0 && end > start) {
        parsed = JSON.parse(cleaned.slice(start, end + 1));
      }
    }
    if (!parsed || typeof parsed !== 'object') return null;
    const points = Array.isArray(parsed.summaryPoints) ? parsed.summaryPoints : [];
    const challenge = parsed.microChallenge || {};
    const options = Array.isArray(challenge.options) ? challenge.options : [];
    const correctIndex = Number.isInteger(challenge.correctIndex) ? challenge.correctIndex : -1;

    if (typeof parsed.hook !== 'string') return null;
    if (points.length < 3) return null;
    if (typeof challenge.question !== 'string') return null;
    if (options.length !== 4) return null;
    if (correctIndex < 0 || correctIndex > 3) return null;

    return {
      hook: parsed.hook.trim(),
      summaryPoints: points.map((x) => String(x || '').trim()).filter(Boolean).slice(0, 3),
      microChallenge: {
        question: String(challenge.question || '').trim(),
        options: options.map((x) => String(x || '').trim()),
        correctIndex,
        hint: String(challenge.hint || '').trim(),
      },
    };
  } catch {
    return null;
  }
}

function getApiKey() {
  return process.env.EXPO_PUBLIC_OPENAI_API_KEY || '';
}

async function callChatCompletion(messages, temperature = 0.7, jsonMode = false) {
  const apiKey = getApiKey();
  if (!apiKey) {
    setLastMentorError('Missing EXPO_PUBLIC_OPENAI_API_KEY');
    return null;
  }

  let res;
  try {
    res = await fetch('https://api.openai.com/v1/chat/completions', {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${apiKey}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        model: 'gpt-4o-mini',
        temperature,
        max_tokens: jsonMode ? 420 : 220,
        ...(jsonMode ? { response_format: { type: 'json_object' } } : {}),
        messages,
      }),
    });
  } catch (err) {
    setLastMentorError(`Network error: ${String(err?.message || err)}`);
    return null;
  }

  let data = null;
  try {
    data = await res.json();
  } catch {
    data = null;
  }

  if (!res.ok) {
    const apiMsg = data?.error?.message || `HTTP ${res.status}`;
    setLastMentorError(`OpenAI API error: ${apiMsg}`);
    return null;
  }

  const content = data?.choices?.[0]?.message?.content || null;
  if (!content) {
    setLastMentorError('OpenAI response has empty content');
    return null;
  }
  setLastMentorError('');
  return content;
}

export async function generateMentorSession({ lesson, studentName, failCount }) {
  const userPrompt = [
    `Eleve: ${studentName || 'Eleve'}`,
    `Matiere: ${lesson.subjectLabel}`,
    `Chapitre: ${lesson.title}`,
    `Resume de lecon: ${lesson.summary || ''}`,
    `Points cles: ${(lesson.keyPoints || []).join(' | ')}`,
    `Echecs consecutifs: ${failCount || 0}`,
    'Genere maintenant hook + summaryPoints + microChallenge en JSON.',
  ].join('\n');

  try {
    setLastMentorError('');
    const content = await callChatCompletion(
      [
        { role: 'system', content: SYSTEM_PROMPT_GRAND_FRERE },
        { role: 'user', content: userPrompt },
      ],
      0.75,
      true
    );
    if (!content) return null;
    const parsed = parseSessionPayload(content);
    if (!parsed) {
      setLastMentorError('LLM response JSON parse failed');
      return null;
    }
    return parsed;
  } catch (err) {
    setLastMentorError(`Session generation error: ${String(err?.message || err)}`);
    return null;
  }
}

export async function generateMentorNudge({
  lesson,
  studentName,
  isCorrect,
  attempts,
  selectedOption,
  question,
}) {
  const outcome = isCorrect ? 'reussite' : 'echec';
  const apiKey = getApiKey();
  if (!apiKey) {
    setLastMentorError('Missing EXPO_PUBLIC_OPENAI_API_KEY');
    return null;
  }

  const userPrompt = [
    `Eleve: ${studentName || 'Eleve'}`,
    `Matiere: ${lesson.subjectLabel}`,
    `Chapitre: ${lesson.title}`,
    `Question: ${question}`,
    `Reponse choisie: ${selectedOption || ''}`,
    `Tentative numero: ${attempts}`,
    `Statut: ${outcome}`,
    'Donne un feedback naturel (2 a 3 phrases max), sans donner la reponse, et termine par une question.',
  ].join('\n');

  try {
    const content = await callChatCompletion(
      [
        { role: 'system', content: SYSTEM_PROMPT_GRAND_FRERE },
        { role: 'user', content: userPrompt },
      ],
      0.8,
      false
    );
    return content ? String(content).trim() : null;
  } catch (err) {
    setLastMentorError(`Nudge generation error: ${String(err?.message || err)}`);
    return null;
  }
}

export async function answerCourseQuestion({ lesson, studentName, question }) {
  const apiKey = getApiKey();
  if (!apiKey) {
    setLastMentorError('Missing EXPO_PUBLIC_OPENAI_API_KEY');
    return null;
  }

  const userPrompt = [
    `Eleve: ${studentName || 'Eleve'}`,
    `Matiere: ${lesson.subjectLabel}`,
    `Chapitre: ${lesson.title}`,
    `Question eleve: ${question}`,
    `Contexte cours: ${lesson.summary || ''}`,
    'Explique la notion en francais simple, naturel, avec exemple local mauritanien. 3 courts paragraphes max et finis par une question.',
  ].join('\n');

  try {
    const content = await callChatCompletion(
      [
        { role: 'system', content: SYSTEM_PROMPT_GRAND_FRERE },
        { role: 'user', content: userPrompt },
      ],
      0.8,
      false
    );
    return content ? String(content).trim() : null;
  } catch (err) {
    setLastMentorError(`Course answer error: ${String(err?.message || err)}`);
    return null;
  }
}

export async function chatWithMentorSimple({
  lesson,
  studentName,
  question,
  recentHistory = [],
}) {
  const apiKey = getApiKey();
  if (!apiKey) {
    setLastMentorError('Missing EXPO_PUBLIC_OPENAI_API_KEY');
    return null;
  }

  const historyText = recentHistory
    .slice(-6)
    .map((m) => `${m.role === 'user' ? 'Eleve' : 'Major'}: ${m.text}`)
    .join('\n');

  const userPrompt = [
    `Eleve: ${studentName || 'Eleve'}`,
    `Matiere: ${lesson.subjectLabel}`,
    `Chapitre: ${lesson.title}`,
    `Question eleve: ${question}`,
    `Contexte cours: ${lesson.summary || ''}`,
    'Historique recent:',
    historyText || '(aucun)',
    'Consignes de style strictes:',
    '- Reponse tres simple',
    '- Maximum 2 phrases courtes',
    '- Aucun detail inutile',
    '- Termine par UNE question de guidage',
    '- Ne donne pas la reponse finale directement',
  ].join('\n');

  try {
    const content = await callChatCompletion(
      [
        { role: 'system', content: SYSTEM_PROMPT_GRAND_FRERE },
        { role: 'user', content: userPrompt },
      ],
      0.65,
      false
    );
    return content ? String(content).trim() : null;
  } catch (err) {
    setLastMentorError(`Simple chat error: ${String(err?.message || err)}`);
    return null;
  }
}

export function isMentorLLMConfigured() {
  return Boolean(getApiKey());
}
