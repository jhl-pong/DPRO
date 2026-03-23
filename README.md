# DPRO

![visitors](https://visitor-badge.laobi.icu/badge?page_id=Evolutionary-Intelligence.DPRO)
[![WeChat](https://img.shields.io/badge/WeChat-07C160?logo=wechat&logoColor=white)](https://github.com/Evolutionary-Intelligence/pypop-docs/blob/main/WeChat/WeChat-20250917.jpg)

## User Profile

The `user_profile` module provides a `UserProfile` class for managing user information.

### Usage

```python
from user_profile import UserProfile

# Create a new profile
profile = UserProfile(
    username="alice",
    email="alice@example.com",
    display_name="Alice",
    bio="Researcher in evolutionary intelligence.",
)

# Update mutable fields
profile.update(bio="Updated bio.", preferences={"theme": "dark"})

# Serialise / deserialise
data = profile.to_dict()
restored = UserProfile.from_dict(data)
```

### Running tests

```bash
python -m pytest test_user_profile.py -v
```
