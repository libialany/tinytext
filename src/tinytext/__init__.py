from __future__ import annotations

try:
    # Python 3.8+
    import importlib.metadata as importlib_metadata
except ImportError:
    # Python 3.7 and lower
    import importlib_metadata  # type: ignore

__version__ = importlib_metadata.version(__name__)


__all__ = ["__version__"]

tiny_letters: dict[int, str] = {
    ord("a"): "ᵃ",
    ord("b"): "ᵇ",
    ord("c"): "ᶜ",
    ord("d"): "ᵈ",
    ord("e"): "ᵉ",
    ord("f"): "ᶠ",
    ord("g"): "ᵍ",
    ord("h"): "ʰ",
    ord("i"): "ᶦ",
    ord("j"): "ʲ",
    ord("k"): "ᵏ",
    ord("l"): "ᶫ",
    ord("m"): "ᵐ",
    ord("n"): "ᶰ",
    ord("o"): "ᵒ",
    ord("p"): "ᵖ",
    ord("q"): "ᑫ",
    ord("r"): "ʳ",
    ord("s"): "ˢ",
    ord("t"): "ᵗ",
    ord("u"): "ᵘ",
    ord("v"): "ᵛ",
    ord("w"): "ʷ",
    ord("x"): "ˣ",
    ord("y"): "ʸ",
    ord("z"): "ᶻ",
    ord("A"): "ᴬ",
    ord("B"): "ᴮ",
    ord("C"): "ᶜ",
    ord("D"): "ᴰ",
    ord("E"): "ᴱ",
    ord("F"): "ᶠ",
    ord("G"): "ᴳ",
    ord("H"): "ᴴ",
    ord("I"): "ᴵ",
    ord("J"): "ᴶ",
    ord("K"): "ᴷ",
    ord("L"): "ᴸ",
    ord("M"): "ᴹ",
    ord("N"): "ᴺ",
    ord("O"): "ᴼ",
    ord("P"): "ᴾ",
    ord("Q"): "ᑫ",
    ord("R"): "ᴿ",
    ord("S"): "ˢ",
    ord("T"): "ᵀ",
    ord("U"): "ᵁ",
    ord("V"): "ⱽ",
    ord("W"): "ᵂ",
    ord("X"): "ˣ",
    ord("Y"): "ʸ",
    ord("Z"): "ᶻ",
    ord("`"): "`",
    ord("~"): "~",
    ord("!"): "﹗",
    ord("@"): "@",
    ord("#"): "#",
    ord("$"): "﹩",
    ord("%"): "﹪",
    ord("^"): "^",
    ord("&"): "﹠",
    ord("*"): "﹡",
    ord("("): "⁽",
    ord(")"): "⁾",
    ord("_"): "⁻",
    ord("-"): "⁻",
    ord("="): "⁼",
    ord("+"): "+",
    ord("{"): "{",
    ord("["): "[",
    ord("}"): "}",
    ord("]"): "]",
    ord(":"): "﹕",
    ord(";"): "﹔",
    ord("?"): "﹖",
}


def tinytext(big: str) -> str:
    """convert your text ᶦᶰᵗᵒ ᵗᶦᶰᶦᵉʳ ᵗᵉˣᵗ"""
    tiny: str = big.translate(tiny_letters)
    return tiny


# End of file
