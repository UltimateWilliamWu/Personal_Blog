const U200D = String.fromCharCode(8205)
const UFE0Fg = /\uFE0F/g
const U20E3 = "\u20E3"

export function getIconCode(char: string) {
  // Keycaps (1\uFE0F\u20E3 = 0031 FE0F 20E3) are keyed *with* their variation selector in
  // the emoji map, so stripping FE0F the way we do for other sequences would
  // produce a codepoint that isn't there.
  const keepVariationSelector = char.indexOf(U200D) >= 0 || char.indexOf(U20E3) >= 0
  return toCodePoint(keepVariationSelector ? char : char.replace(UFE0Fg, ""))
}

function toCodePoint(unicodeSurrogates: string) {
  const r = []
  let c = 0,
    p = 0,
    i = 0

  while (i < unicodeSurrogates.length) {
    c = unicodeSurrogates.charCodeAt(i++)
    if (p) {
      r.push((65536 + ((p - 55296) << 10) + (c - 56320)).toString(16))
      p = 0
    } else if (55296 <= c && c <= 56319) {
      p = c
    } else {
      // the map zero-pads to at least 4 hex digits, so BMP codepoints below
      // U+1000 (the ASCII bases of keycap sequences) must be padded to match
      r.push(c.toString(16).padStart(4, "0"))
    }
  }
  return r.join("-")
}

type EmojiMap = {
  codePointToName: Record<string, string>
  nameToBase64: Record<string, string>
}

let emojimap: EmojiMap | undefined = undefined
export async function loadEmoji(code: string) {
  if (!emojimap) {
    const data = await import("./emojimap.json")
    emojimap = data
  }

  const name = emojimap.codePointToName[`${code.toUpperCase()}`]
  if (!name) throw new Error(`codepoint ${code} not found in map`)

  const b64 = emojimap.nameToBase64[name]
  if (!b64) throw new Error(`name ${name} not found in map`)

  return b64
}
