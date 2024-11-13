import pandas as pd

def sort_csv(file_path, ascending=True):
    """
    Hàm sắp xếp file CSV theo cột Date và cột Country/Region.
    file_path: Đường dẫn đến file CSV đầu vào.
    ascending: Thứ tự sắp xếp, True là tăng dần, False là giảm dần.
    """
    # Đọc dữ liệu từ file CSV
    df = pd.read_csv(file_path)
    print(df.columns)

    if ascending == 'false':
        ascending = False
    else:
        ascending = True
    # Sắp xếp dữ liệu theo cột chỉ định
    sort_column = ['Date', 'Country/Region']
    df_sorted = df.sort_values(by=sort_column, ascending=ascending)

    # Lưu lại DataFrame đã sắp xếp vào file CSV
    df_sorted.to_csv(file_path, index=False)

    print(f"Dữ liệu đã được sắp xếp theo cột '{sort_column}' và lưu vào '{file_path}'.")

if __name__ == "__main__":
    file_path = input("Nhập đường dẫn tới file CSV: ")
    order = input("Sắp xếp tăng dần(True) hoặc giảm dần(False): ").strip().lower()
    sort_csv(file_path, order)
