"""User profile module for DPRO."""

import re
from dataclasses import dataclass, field
from typing import Optional

_EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


@dataclass
class UserProfile:
    """Represents a user profile in the DPRO application."""

    username: str
    email: str
    display_name: Optional[str] = None
    bio: Optional[str] = None
    avatar_url: Optional[str] = None
    preferences: dict = field(default_factory=dict)

    def __post_init__(self):
        if not self.username:
            raise ValueError("username cannot be empty")
        if not self.email or not _EMAIL_RE.match(self.email):
            raise ValueError("Valid email address is required")
        if self.display_name is None:
            self.display_name = self.username

    def update(self, **kwargs):
        """Update profile fields. Returns self for chaining."""
        allowed = {"display_name", "bio", "avatar_url", "preferences"}
        for key, value in kwargs.items():
            if key not in allowed:
                raise ValueError(f"'{key}' is not an updatable profile field")
            setattr(self, key, value)
        return self

    def to_dict(self):
        """Return the profile as a plain dictionary."""
        return {
            "username": self.username,
            "email": self.email,
            "display_name": self.display_name,
            "bio": self.bio,
            "avatar_url": self.avatar_url,
            "preferences": self.preferences,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "UserProfile":
        """Create a UserProfile from a dictionary."""
        return cls(
            username=data["username"],
            email=data["email"],
            display_name=data.get("display_name"),
            bio=data.get("bio"),
            avatar_url=data.get("avatar_url"),
            preferences=data.get("preferences", {}),
        )
