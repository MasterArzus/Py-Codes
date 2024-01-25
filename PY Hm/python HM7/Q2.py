import pandas as pd

ser1 = pd.Series(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                  'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                  'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                  'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                  'V', 'W', 'X', 'Y', 'Z'])
ser2 = pd.Series([i for i in range(1, 27)])
print(ser1)
print(ser2)
ser_df1 = pd.DataFrame({'letter': ser1, 'number': ser2})
print(ser_df1)
ser_df2 = pd.DataFrame({'letter': ser1, 'number': ser2})
print(ser_df2.fillna(-1))
