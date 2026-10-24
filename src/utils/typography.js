// Vertical rhythm helpers, matching the values the old typography.js
// "Wordpress2016" theme produced. Its generated CSS is now static in
// src/styles/typography.css.

const BASE_FONT_SIZE = 16 // px
const BASE_LINE_HEIGHT = 1.75
const SCALE_RATIO = 5 / 2
const MIN_LINE_PADDING = 2 // px

const LINE_HEIGHT_PX = BASE_FONT_SIZE * BASE_LINE_HEIGHT

const toRem = (px) => `${parseFloat((px / BASE_FONT_SIZE).toFixed(5))}rem`

export const rhythm = (lines = 1) => toRem(lines * LINE_HEIGHT_PX)

// Number of lines (to the nearest half line) a font size needs
const linesForFontSize = (fontPx) => {
  let lines = Math.ceil((2 * fontPx) / LINE_HEIGHT_PX) / 2
  if (lines * LINE_HEIGHT_PX - fontPx < 2 * MIN_LINE_PADDING) {
    lines += 0.5
  }
  return lines
}

export const scale = (value) => {
  const fontPx = Math.pow(SCALE_RATIO, value) * BASE_FONT_SIZE
  return {
    fontSize: toRem(fontPx),
    lineHeight: rhythm(linesForFontSize(fontPx)),
  }
}
