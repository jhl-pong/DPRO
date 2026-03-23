"""Tests for the user_profile module."""

import pytest
from user_profile import UserProfile


def test_create_basic_profile():
    profile = UserProfile(username="alice", email="alice@example.com")
    assert profile.username == "alice"
    assert profile.email == "alice@example.com"
    assert profile.display_name == "alice"
    assert profile.bio is None
    assert profile.avatar_url is None
    assert profile.preferences == {}


def test_display_name_defaults_to_username():
    profile = UserProfile(username="bob", email="bob@example.com")
    assert profile.display_name == "bob"


def test_explicit_display_name():
    profile = UserProfile(username="bob", email="bob@example.com", display_name="Bob Smith")
    assert profile.display_name == "Bob Smith"


def test_empty_username_raises():
    with pytest.raises(ValueError, match="username cannot be empty"):
        UserProfile(username="", email="x@example.com")


def test_invalid_email_raises():
    with pytest.raises(ValueError, match="[Vv]alid email"):
        UserProfile(username="alice", email="not-an-email")


def test_empty_email_raises():
    with pytest.raises(ValueError, match="[Vv]alid email"):
        UserProfile(username="alice", email="")


def test_malformed_email_raises():
    for bad in ("@example.com", "user@", "user@@example.com", "user@example"):
        with pytest.raises(ValueError, match="[Vv]alid email"):
            UserProfile(username="alice", email=bad)


def test_update_allowed_fields():
    profile = UserProfile(username="alice", email="alice@example.com")
    profile.update(bio="Hello!", avatar_url="https://example.com/avatar.png")
    assert profile.bio == "Hello!"
    assert profile.avatar_url == "https://example.com/avatar.png"


def test_update_returns_self():
    profile = UserProfile(username="alice", email="alice@example.com")
    result = profile.update(bio="Hello!")
    assert result is profile


def test_update_disallowed_field_raises():
    profile = UserProfile(username="alice", email="alice@example.com")
    with pytest.raises(ValueError, match="not an updatable profile field"):
        profile.update(username="hacker")


def test_to_dict():
    profile = UserProfile(
        username="alice",
        email="alice@example.com",
        display_name="Alice",
        bio="Bio text",
        preferences={"theme": "dark"},
    )
    d = profile.to_dict()
    assert d["username"] == "alice"
    assert d["email"] == "alice@example.com"
    assert d["display_name"] == "Alice"
    assert d["bio"] == "Bio text"
    assert d["preferences"] == {"theme": "dark"}


def test_from_dict_roundtrip():
    data = {
        "username": "carol",
        "email": "carol@example.com",
        "display_name": "Carol",
        "bio": "Hi",
        "avatar_url": "https://example.com/carol.png",
        "preferences": {"lang": "zh"},
    }
    profile = UserProfile.from_dict(data)
    assert profile.to_dict() == data


def test_from_dict_minimal():
    profile = UserProfile.from_dict({"username": "dave", "email": "dave@example.com"})
    assert profile.username == "dave"
    assert profile.display_name == "dave"
    assert profile.preferences == {}
