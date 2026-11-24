from dataclasses import dataclass, field

lazy from jumpedia.interfaces.dsls.core.errors.eval import AnyEvalErrorT
lazy from jumpedia.interfaces.dsls.core.errors.lex import AnyLexErrorT
lazy from jumpedia.interfaces.dsls.core.errors.parse import AnyParseErrorT

type AnyDslErrorT = AnyEvalErrorT | AnyLexErrorT | AnyParseErrorT


@dataclass()
class DslError(Exception):
    """Base class of all DSL errors."""

    # Number and text of the line of a file the error happened in.
    file_line: tuple[int, str] | None = field(default=None, kw_only=True)
