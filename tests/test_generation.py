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


@pytest.mark.parametrize(
    "id_hex,id_str",
    [
        ("0665635762607e9c8000b0d2d9e3c106", "user_novdr227c7J1x4q3PYJS1"),
        ("0665635762607e9d15aaaaaabbbbcccc", "user_novdr227c7j3stXTQ3Vg7"),
        ("0665639bd67f7e9f8000ada40acde041", "user_novjYiLxio6FsNHrR7VHa"),
        ("0665639e19187e438000ce7f4a511b9e", "user_novjjddFdGE2Ljfa4qWWh"),
    ],
)
def test_encode_hard(id_hex, id_str):
    typeids = generate("user")
    id = typeids.UserId(id_hex)
    assert id.hex == id_hex
    assert str(id) == id_str

    assert id.hex == typeids.UserId(id.hex).hex
    assert id.hex == typeids.UserId(id.bytes).hex
    assert id.hex == typeids.UserId(str(id)).hex
    assert str(id) == str(typeids.UserId(id.hex))
    assert str(id) == str(typeids.UserId(id.bytes))
    assert str(id) == str(typeids.UserId(str(id)))


def test_encode_random():
    typeids = generate("user", generator=lambda: uuid7().hex)
    id = typeids.UserId()

    assert id.hex == typeids.UserId(id.hex).hex
    assert id.hex == typeids.UserId(id.bytes).hex
    assert id.hex == typeids.UserId(str(id)).hex
    assert str(id) == str(typeids.UserId(id.hex))
    assert str(id) == str(typeids.UserId(id.bytes))
    assert str(id) == str(typeids.UserId(str(id)))
