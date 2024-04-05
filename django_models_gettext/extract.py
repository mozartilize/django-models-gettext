from collections.abc import (
    Collection,
    Generator,
    Mapping,
)
from typing import Any, TYPE_CHECKING

from django.db.models import QuerySet

if TYPE_CHECKING:
    from typing import IO, Final, Protocol

    from _typeshed import SupportsItems, SupportsRead, SupportsReadline
    from typing_extensions import TypeAlias, TypedDict

    class _PyOptions(TypedDict, total=False):
        encoding: str

    class _JSOptions(TypedDict, total=False):
        encoding: str
        jsx: bool
        template_string: bool
        parse_template_string: bool

    class _FileObj(SupportsRead[bytes], SupportsReadline[bytes], Protocol):
        def seek(self, __offset: int, __whence: int = ...) -> int: ...
        def tell(self) -> int: ...

    _SimpleKeyword: TypeAlias = tuple[int | tuple[int, int] | tuple[int, str], ...] | None
    _Keyword: TypeAlias = dict[int | None, _SimpleKeyword] | _SimpleKeyword

    # 5-tuple of (filename, lineno, messages, comments, context)
    _FileExtractionResult: TypeAlias = tuple[str, int, str | tuple[str, ...], list[str], str | None]

    # 4-tuple of (lineno, message, comments, context)
    _ExtractionResult: TypeAlias = tuple[int, str | tuple[str, ...], list[str], str | None]


class DjangoModelExtractor:
    pass



def extract_django_models(
    queryset: QuerySet,
    keywords: Mapping[str, _Keyword],
    comment_tags: Collection[str],
    options: Mapping[str, Any],
) -> Generator[_ExtractionResult, None, None]:
    fields = queryset.model._meta.translation.fields
    for record in queryset:
        for field in fields:
            yield (0, getattr(record, field), [], None)