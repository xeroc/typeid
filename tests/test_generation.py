import pytest
from uuid_extensions import uuid7
from typeid import generate


def test_generation():
    typeids = generate("sk", "pk", "user", "apikey")
    assert str(typeids.SkId(uuid7().hex)).startswith("sk_")
    assert str(typeids.PkId(uuid7().hex)).startswith("pk_")
    assert str(typeids.UserId(uuid7().hex)).startswith("user_")
    assert str(typeids.ApikeyId(uuid7().hex)).startswith("apikey_")
    assert (
        typeids.UserId("user_nnv5rr3rfk3hgry6xrygr").hex
        == "0664c4135ed83faabd4bc0dc33839c9f"
    )
    extra_types = generate("admin", suffix="IdUseWithCare")
    assert str(extra_types.AdminIdUseWithCare(uuid7().hex)).startswith("admin_")


def test_wrong_prefix():
    typeids = generate("sk", "user")
    with pytest.raises(ValueError):
        typeids.UserId("sk_nnv5rr3rfk3hgry6xrygr")


def test_typed_id_with_generator():
    typeids = generate("user", generator=lambda: uuid7().hex)
    user_id = typeids.UserId()
