// Thème Major 6AF — Mauritanie 🇲🇷
// Couleurs de la marque Major (bleu) + culture mauritanienne (or, chameau)

export const COLORS = {
  // Brand Major — bleu royal
  primary: '#2563eb',
  primaryDark: '#182b66',
  primaryLight: '#38bdf8',

  // Or Major / mauritanien
  gold: '#F0B429',
  goldLight: '#fde68a',

  // Mauritanie accent
  mauritaniaGreen: '#06803C',
  mauritaniaRed: '#CC1A1A',

  // Matières
  french: '#38bdf8',
  math: '#fb923c',
  science: '#34d399',

  // UI
  background: '#f0f4ff',
  surface: '#ffffff',
  ink: '#0f172a',
  muted: '#64748b',
  border: 'rgba(37,99,235,0.10)',
  shadow: 'rgba(24,43,102,0.14)',

  // Feedback
  success: '#10b981',
  error: '#ef4444',
  warning: '#F0B429',
};

export const GRADIENTS = {
  hero:      ['#182b66', '#2563eb', '#38bdf8'],
  heroAlt:   ['#182b66', '#1e40af'],
  challenge: ['#1e1b4b', '#4338ca'],
  gold:      ['#F0B429', '#fb923c'],
  success:   ['#059669', '#10b981'],
  french:    ['#0284c7', '#38bdf8'],
  math:      ['#ea580c', '#fb923c'],
  science:   ['#059669', '#34d399'],
};

export const SHADOWS = {
  card: {
    shadowColor: '#182b66',
    shadowOffset: { width: 0, height: 6 },
    shadowOpacity: 0.10,
    shadowRadius: 16,
    elevation: 6,
  },
  button: {
    shadowColor: '#2563eb',
    shadowOffset: { width: 0, height: 6 },
    shadowOpacity: 0.35,
    shadowRadius: 12,
    elevation: 8,
  },
};

export const LEVELS = [
  { id: 'beginner',     label: 'Débutant',     labelAr: 'مبتدئ',  color: '#94a3b8', min: 0,   max: 39,  icon: '🌱' },
  { id: 'intermediate', label: 'Intermédiaire', labelAr: 'متوسط',  color: '#fb923c', min: 40,  max: 69,  icon: '⭐' },
  { id: 'advanced',     label: 'Avancé',        labelAr: 'متقدم',  color: '#2563eb', min: 70,  max: 84,  icon: '🚀' },
  { id: 'expert',       label: 'Expert',        labelAr: 'خبير',   color: '#F0B429', min: 85,  max: 100, icon: '🏆' },
];
