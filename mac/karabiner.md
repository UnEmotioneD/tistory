# Karaniber

Karabiner Complex Rules

---

## Table of Contents

- [Caps Lock](#caps-lock)
- [esc to Caps](#esc-to-caps)
- [Right Command](#right-command)
- [Media Control](#media-control)

---

## Caps Lock

```json
{
  "description": "Caps Lock to Control / Escape if pressed alone",
  "manipulators": [
    {
      "from": {
        "key_code": "caps_lock",
        "modifiers": {
          "optional": ["any"]
        }
      },
      "to": [
        {
          "key_code": "left_control"
        }
      ],
      "to_if_alone": [
        {
          "key_code": "escape"
        }
      ],
      "type": "basic"
    }
  ]
}
```

---

## ESC to Caps

```json
{
  "description": "ESC to caps lock",
  "manipulators": [
    {
      "from": {
        "key_code": "escape",
        "modifiers": {
          "optional": ["any"]
        }
      },
      "to": [
        {
          "key_code": "caps_lock"
        }
      ],
      "type": "basic"
    }
  ]
}
```

---

## Right Command

```json
{
  "description": "right_command to fn / f16 if pressed alone",
  "manipulators": [
    {
      "from": {
        "key_code": "right_command",
        "modifiers": { "optional": ["any"] }
      },
      "to": [{ "key_code": "fn" }],
      "to_if_alone": [{ "key_code": "f16" }],
      "type": "basic"
    }
  ]
}
```

---

## Media Control

```json
{
  "description": "Enhanced Media Controls with Fn Key",
  "manipulators": [
    {
      "from": {
        "key_code": "spacebar",
        "modifiers": {
          "mandatory": ["fn"]
        }
      },
      "to": [
        {
          "consumer_key_code": "play_or_pause"
        }
      ],
      "type": "basic"
    },
    {
      "from": {
        "key_code": "left_arrow",
        "modifiers": {
          "mandatory": ["fn"]
        }
      },
      "to": [
        {
          "consumer_key_code": "rewind"
        }
      ],
      "type": "basic"
    },
    {
      "from": {
        "key_code": "right_arrow",
        "modifiers": {
          "mandatory": ["fn"]
        }
      },
      "to": [
        {
          "consumer_key_code": "fast_forward"
        }
      ],
      "type": "basic"
    },
    {
      "from": {
        "key_code": "up_arrow",
        "modifiers": {
          "mandatory": ["fn"]
        }
      },
      "to": [
        {
          "consumer_key_code": "volume_increment"
        }
      ],
      "type": "basic"
    },
    {
      "from": {
        "key_code": "down_arrow",
        "modifiers": {
          "mandatory": ["fn"]
        }
      },
      "to": [
        {
          "consumer_key_code": "volume_decrement"
        }
      ],
      "type": "basic"
    },
    {
      "from": {
        "key_code": "m",
        "modifiers": {
          "mandatory": ["fn"]
        }
      },
      "to": [
        {
          "consumer_key_code": "mute"
        }
      ],
      "type": "basic"
    }
  ]
}
```
