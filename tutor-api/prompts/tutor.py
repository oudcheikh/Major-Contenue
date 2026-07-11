MENTOR_SYSTEM = """Tu es Major, un mentor educatif mauritanien.
Identite : Grand frere bienveillant, encourageant et drole.
Public : Eleves de CM2 en Mauritanie preparant le concours 6AF.

Regles :
1. NE DONNE JAMAIS LA REPONSE directement. Guide l'eleve par des questions.
2. Utilise des exemples locaux mauritaniens (Nouakchott, le desert, le marche, la peche, le chameau).
3. Francais simple. Glisse un mot en Hassanya pour encourager ("Macha Allah", "Zine", "Bravo champion").
4. Reponses COURTES et PRECISES. Maximum 3 phrases par bloc.
5. Pour les calculs, sois TOUJOURS exact et verifie tes resultats.""".strip()

SESSION_FORMAT = """Retourne UNIQUEMENT un JSON valide (sans markdown, sans ```):
{
  "hook": "accroche courte (2-3 phrases max, finit par une question)",
  "summaryPoints": ["point 1", "point 2", "point 3"],
  "microChallenge": {
    "question": "question QCM",
    "options": ["A", "B", "C", "D"],
    "correctIndex": 0,
    "hint": "indice sans donner la reponse"
  }
}""".strip()


def build_session_prompt(lesson_context: str, student_name: str = "Eleve") -> list[dict]:
    return [
        {"role": "system", "content": MENTOR_SYSTEM},
        {
            "role": "user",
            "content": (
                f"Eleve: {student_name}\n"
                f"{lesson_context}\n\n"
                f"Genere une session de tutorat sur cette lecon.\n"
                f"{SESSION_FORMAT}"
            ),
        },
    ]


def build_nudge_prompt(
    lesson_context: str,
    question: str,
    selected_option: str,
    is_correct: bool,
    attempts: int,
    student_name: str = "Eleve",
) -> list[dict]:
    outcome = "reussite" if is_correct else "echec"
    return [
        {"role": "system", "content": MENTOR_SYSTEM},
        {
            "role": "user",
            "content": (
                f"Eleve: {student_name}\n"
                f"{lesson_context}\n"
                f"Question: {question}\n"
                f"Reponse choisie: {selected_option}\n"
                f"Tentative numero: {attempts}\n"
                f"Statut: {outcome}\n\n"
                "Donne un feedback naturel (2-3 phrases max). "
                "Ne donne pas la reponse. Termine par une question de guidage."
            ),
        },
    ]


def build_question_prompt(
    lesson_context: str,
    student_question: str,
    student_name: str = "Eleve",
) -> list[dict]:
    return [
        {"role": "system", "content": MENTOR_SYSTEM},
        {
            "role": "user",
            "content": (
                f"Eleve: {student_name}\n"
                f"{lesson_context}\n"
                f"Question de l'eleve: {student_question}\n\n"
                "Explique en francais simple avec un exemple mauritanien. "
                "3 paragraphes courts max. Finis par une question."
            ),
        },
    ]


def build_chat_prompt(
    lesson_context: str,
    student_question: str,
    history: list[dict] | None = None,
    student_name: str = "Eleve",
) -> list[dict]:
    history_text = ""
    if history:
        history_text = "\n".join(
            f"{'Eleve' if m.get('role') == 'user' else 'Major'}: {m.get('content', m.get('text', ''))}"
            for m in history[-6:]
        )

    return [
        {"role": "system", "content": MENTOR_SYSTEM},
        {
            "role": "user",
            "content": (
                f"Eleve: {student_name}\n"
                f"{lesson_context}\n"
                f"Question: {student_question}\n"
                f"Historique:\n{history_text or '(aucun)'}\n\n"
                "Reponds en 2 phrases courtes max. "
                "Ne donne pas la reponse finale. "
                "Termine par UNE question de guidage."
            ),
        },
    ]


def get_tutor_prompt(lang: str = "fr") -> str:
    """Backward-compatible: used by the generic /chat endpoint."""
    return MENTOR_SYSTEM
