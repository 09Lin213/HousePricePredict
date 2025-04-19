import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# 讀取 Excel 資料（記得先安裝 openpyxl 套件）
df = pd.read_excel('house_data.xlsx', engine='openpyxl')

# 確認資料沒問題
print(df.head())

# 設定特徵（X）與目標（y）
X = df[['坪數', '樓層']]  # 如果有其他欄位也可以加入，例如：屋齡、區域等
y = df['房價']

# 分割資料集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 建立模型
model = LinearRegression()
model.fit(X_train, y_train)

# 假設要預測一間 40 坪、5 樓的房子價格
predict_price = model.predict([[40, 5]])
print(f"預估房價：約 {predict_price[0]:.2f} 萬元")