# Dock

## Dock Popout Speed

dock popout speed to 0 sec delay
hide doc as soon as pointer leaves the dock area
restart dock

```bash
defaults write com.apple.dock autohide-delay -int 0
defaults write com.apple.dock autohide-time-modifier -float 0.1
killall Dock
```

## Reset Dock Popout Speed

pass default values

```bash
defaults delete com.apple.dock autohide-delay
defaults delete com.apple.dock autohide-time-modifier
killall Dock
```

## Create Transparent Bar Inside Dock

```bash
defaults write com.apple.dock persistent-apps -array-add '{"tile-type"="small-spacer-tile";}'; killall Dock
```

## Reset Dock

```bash
defaults delete com.apple.dock; killall Dock
```
