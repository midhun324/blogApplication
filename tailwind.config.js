/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',  // Django HTML templates
    './static/**/*.js',       // Static JS files
    './static/css/**/*.css',  // Static CSS files
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
