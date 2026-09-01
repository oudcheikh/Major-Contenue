// URLs des 37 vidéos explicatives (31 maths + 6 sciences), servies en
// streaming direct (HTTP 200 + Range, sans redirection) par le CDN de
// raw.githubusercontent.com — dépôt oudcheikh/major-videos. Les mêmes
// fichiers restent en secours sur la release major-releases/videos-v1.
// Nécessite une connexion internet — le reste de la leçon marche hors ligne.

const VIDEO_BASE = 'https://raw.githubusercontent.com/oudcheikh/major-videos/main'

export function getVideoUrl(lessonId) {
  let m = lessonId.match(/^math6-u(\d{2})$/)
  if (m) return `${VIDEO_BASE}/Major-Math-U${m[1]}-1080p.mp4`
  m = lessonId.match(/^sci6-u(\d)$/)
  if (m) return `${VIDEO_BASE}/Major-Science-S0${m[1]}-1080p.mp4`
  return null
}
