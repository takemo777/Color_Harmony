import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors

# HEXからRGBへの変換
def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

# RGBからHEXへの変換
def rgb_to_hex(rgb):
    return "#{0:02x}{1:02x}{2:02x}".format(*rgb)

# RGBからHSVへの変換
def rgb_to_hsv(r, g, b):
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx - mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g - b) / df) + 360) % 360
    elif mx == g:
        h = (60 * ((b - r) / df) + 120) % 360
    elif mx == b:
        h = (60 * ((r - g) / df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = df / mx
    v = mx
    return h, s, v

# HSVからRGBへの変換
def hsv_to_rgb(h, s, v):
    h = float(h)
    s = float(s)
    v = float(v)
    h60 = h / 60.0
    h60f = np.floor(h60)
    hi = int(h60f) % 6
    f = h60 - h60f
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)
    if hi == 0:
        r, g, b = v, t, p
    elif hi == 1:
        r, g, b = q, v, p
    elif hi == 2:
        r, g, b = p, v, t
    elif hi == 3:
        r, g, b = p, q, v
    elif hi == 4:
        r, g, b = t, p, v
    elif hi == 5:
        r, g, b = v, p, q
    r, g, b = int(r * 255), int(g * 255), int(b * 255)
    return r, g, b

# 調和色の生成
def harmonious_color_combination(base_hue):
    colors = []
    color_codes = []
    for i in range(4):
        hue = (base_hue + i * 0.25) % 1.0 # 色相環上で等間隔に色相を設定
        saturation = 0.7 # 彩度は高めに設定
        lightness = 0.5 if i % 2 == 0 else 0.7 # 明度を交互に変更
        color = mcolors.hsv_to_rgb([hue, saturation, lightness])
        rgb_code = rgb_to_hex((int(color[0]*255), int(color[1]*255), int(color[2]*255)))
        color_codes.append(rgb_code)
    return color_codes

# 入力色
base_code = "#FF0000"
base_color_rgb = hex_to_rgb(base_code)

# HSV変換
h, s, v = rgb_to_hsv(*base_color_rgb)

# 調和色と相性の良い色を生成
complementary_color = rgb_to_hex(hsv_to_rgb((h + 180) % 360, s, v)) # 補色
analogous_color1 = rgb_to_hex(hsv_to_rgb((h + 30) % 360, s, v)) # 類似色1
analogous_color2 = rgb_to_hex(hsv_to_rgb((h - 30) % 360, s, v)) # 類似色2
triadic_color1 = rgb_to_hex(hsv_to_rgb((h + 120) % 360, s, v)) # 三角色1
triadic_color2 = rgb_to_hex(hsv_to_rgb((h - 120) % 360, s, v)) # 三角色2
color_codes_fashion = harmonious_color_combination(h / 360) # 独自

# すべてのカラーコードを合わせる
all_colors = [base_code, complementary_color, analogous_color1, analogous_color2, triadic_color1, triadic_color2] + color_codes_fashion

print(all_colors)

# カラーパレットを表示
plt.figure(figsize=(12, 2))
for i, code in enumerate(all_colors):
    plt.fill_between([i, i+1], 0, 1, color=code)
plt.xlim(0, len(all_colors))
plt.axis("off")
plt.show()
