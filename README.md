# ATTENTION!
# PLEASE USE THE BRAND NEW [FluentUI Pro](https://github.com/zhuzichu520/FluentUI2) INSTEAD!
<div align=center>
  <img width=64 src="doc/preview/fluent_design.svg">
</div>

<h1 align="center">
  QML FluentUI 
</h1>
<p align="center">
  A fluent design component library for Qt QML， You need C++ <a href="https://github.com/zhuzichu520/FluentUI">FluentUI</a>。
</p>

![win-badge] ![ubuntu-badge] ![macos-badge] ![release-badge] ![download-badge] ![download-latest]

<p align="center">
English | <a href="README_zh_CN.md">简体中文</a>
</p>
<div align=center>
  <img src="doc/preview/demo_large.png">
</div>

[win-link]: https://github.com/zhuzichu520/FluentUI/actions?query=workflow%3AWindows "WindowsAction"
[win-badge]: https://github.com/zhuzichu520/FluentUI/workflows/Windows/badge.svg  "Windows"
[ubuntu-link]: https://github.com/zhuzichu520/FluentUI/actions?query=workflow%3AUbuntu "UbuntuAction"
[ubuntu-badge]: https://github.com/zhuzichu520/FluentUI/workflows/Ubuntu/badge.svg "Ubuntu"
[macos-link]: https://github.com/zhuzichu520/FluentUI/actions?query=workflow%3AMacOS "MacOSAction"
[macos-badge]: https://github.com/zhuzichu520/FluentUI/workflows/MacOS/badge.svg "MacOS"
[release-link]: https://github.com/zhuzichu520/FluentUI/releases "Release status"
[release-badge]: https://img.shields.io/github/release/zhuzichu520/FluentUI.svg?style=flat-square "Release status"
[download-link]: https://github.com/zhuzichu520/FluentUI/releases/latest "Download status"
[download-badge]: https://img.shields.io/github/downloads/zhuzichu520/FluentUI/total.svg "Download status"
[download-latest]: https://img.shields.io/github/downloads/zhuzichu520/PySide6-FluentUI-QML/latest/total.svg "latest status"

## Requirements
+ Python 3.x

## ⚽ Get started
+ run `example` program.
```bash
git clone --recursive https://github.com/zhuzichu520/PySide6-FluentUI-QML.git
```

+ Build

```bash
git clone --recursive https://github.com/zhuzichu520/PySide6-FluentUI-QML.git
cd PySide6-FluentUI-QML

# 安装虚拟环境及相关包
python ./script-init-venv.py

# 先更新资源文件和翻译文件，然后启动程序
python ./script-start.py

# 直接启动程序，跳过启动时初始化
python ./script-start.py fast

# 使用nuitka打包
（init-venv.py文件中已注释打包工具，不推荐打包）
python ./script-build-nuitka.py
```

## 📑 Documentations

(Work in progress...🚀)

## Supported components

|Catalog|Detail|Notes / Demos|
|:----:|:----:|:----:|
|FluApp|The initial entry of the program|Router supported(SPA)|
|FluWindow|Frameless Window|*This only works on windows|
|FluAppBar|Title bar on top of the window|Drag, minimize, maximize and close are supported.|
|FluText|Common text||
|FluButton|Common button|![btn](doc/preview/demo_standardbtn.png) |
|FluFilledButton|Filled button|![filledbtn](doc/preview/demo_filledbtn.png)|
|FluTextButton|Text button|![textbtn](doc/preview/demo_textbtn.png)|
|FluToggleButton|Toggle buttons|![togglebtn](doc/preview/demo_toggle_btn.png)|
|FluIcon|Common icon|![icons](doc/preview/demo_icon.png)|
|FluRadioButton|radio button|![radiobtn](doc/preview/demo_radiobtn.png)|
|FluTextBox|Single-line input box|![textbox](doc/preview/demo_textbox.png)|
|FluMultiLineTextBox|Multi-lines input area|![textarea](doc/preview/demo_multiline_textbox.png)|
|FluToggleSwitch|toggle switch|![toggleswitch](doc/preview/demo_toggle_switch.png)|


View more [`here`](doc/md/all_components.md)!

## Reference
+ [**FluentUI for qml**: C++ and QML.](https://github.com/zhuzichu520/FluentUI)
+ [**Windows design**: Design guidelines and toolkits of Microsoft.](https://learn.microsoft.com/en-us/windows/apps/design/)
+ [**Microsoft/WinUI-Gallery**: Microsoft's demo](https://github.com/microsoft/WinUI-Gallery)


## License

This FluentUI library currently licensed under [MIT License](./License)

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=zhuzichu520/PySide6-FluentUI-QML&type=Date)](https://star-history.com/#zhuzichu520/PySide6-FluentUI-QML&Date)

## ⚡ Visitor count
![](https://profile-counter.glitch.me/zhuzichu520-PySide6-FluentUI-QML/count.svg)
