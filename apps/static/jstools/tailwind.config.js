/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['../../../apps/templates/**/*.html',
            '../../templates/*.html'],
  theme: {
    extend: {
      spacing: {
        'custom': '8px',
      }
    },
  },
  plugins: [],
}

