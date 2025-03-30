import tkinter as tk
from tkinter import messagebox as mes

# 定数（変換係数と理想BMI値）
M_CONV = 100
IDEAL_BMI = 22

# BMIを計算する関数
def calculate_bmi(weight, height_m):
    return weight / (height_m ** 2)

# 理想体重を計算する関数
def calculate_ideal_weight(height_m):
    return IDEAL_BMI * (height_m ** 2)

# BMIに基づいて肥満度を判定する関数
def judge_bmi(bmi):
    if bmi < 18.5:
        return "痩せすぎです"
    elif 18.5 <= bmi < 25:
        return "普通体重です"
    elif 25 <= bmi < 30:
        return "肥満（1度）です"
    elif 30 <= bmi < 35:
        return "肥満（2度）です"
    else:
        return "高度肥満（3度以上）です"

# 診断ボタンが押されたときの処理
def on_click():
    try:
        height_cm = float(entry_height.get())
        weight = float(entry_weight.get())

        # 正の数かチェック
        if height_cm <= 0 or weight <= 0:
            raise ValueError

        height_m = height_cm / M_CONV
        bmi = calculate_bmi(weight, height_m)
        ideal = calculate_ideal_weight(height_m)
        judgement = judge_bmi(bmi)

        # 結果を表示
        label_result.config(
            text=f"→ BMI: {bmi:.2f}\n→ 理想体重: {ideal:.2f} kg\n→ 判定: {judgement}"
        )

    except ValueError:
        mes.showerror("入力エラー", "正しい数値を入力してください。")


# ------------------------------
# ウィンドウ本体の作成
# ------------------------------
def make_Window( title = "タイトル", size = "300x200", resizable = False ):
	root = tk.Tk()							# ウィンドウオブジェクトを作成
	root.title(title)						# ウィンドウタイトル
	root.geometry(size)						# ウィンドウサイズ（幅x高さ）
	root.resizable(resizable, resizable)	# ← 引数で制御できるようになっている
	return root

# ------------------------------
# 入力欄を生成する関数
# ------------------------------
def make_input_field(parent, label_text):
    """ラベルと入力欄（Entry）をセットで作成し、Entryを返す"""
    tk.Label(parent, text=label_text).pack(pady=5)
    entry = tk.Entry(parent)
    entry.pack()
    return entry

root = make_Window("💡 BMI診断ツール","300x250",False)

# GUI部品の構築
entry_height = make_input_field(root, "身長 (cm):")
entry_weight = make_input_field(root, "体重 (kg):")

# 診断ボタン
tk.Button(root, text="診断する", command=on_click).pack(pady=10)

# 結果表示ラベル（空の状態で準備）
label_result = tk.Label(root, text="", justify="left")
label_result.pack()

# GUIを起動
root.mainloop()