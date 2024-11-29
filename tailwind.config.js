/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./**/*.{html,py,js}", // Include all HTML, Python, and JS files
    "!./node_modules/**/*", // Exclude everything in node_modules
  ],
  darkMode: 'selector',
  theme: {
    extend: {
      fontFamily: {
        'poppins': ['poppins', 'sans']
      },
      colors: {
        background: "var(--background)",
        foreground: "var(--foreground)",
      },
    },
  },
  plugins: [],
};
