# 📊 LifeReader

Lightweight Python class for parsing and processing custom-formatted time series data from plain text .lif files. It reads dates and corresponding values, handles comments and formatting quirks, and returns a clean, imputed pandas DataFrame indexed by date.

---

## 🧾 Features

- Parses human-friendly time series data with lines like `14 - 3.2` under monthly/year headers.
- Accepts a file path or list of file paths.
- Ignores inline comments beginning with `#`.
- Supports custom data types (default: `float`).
- Fills missing dates with a specified value (default: 0). (Future: interpolate data values)
- Returns a tidy DataFrame indexed by `datetime.date`.

---

## 📦 Dependencies

- `numpy`
- `pandas`
- `datetime`
- `re` (built-in)

---

## 🧪 Example Usage
```
lr = LifeReader()
lr.read(['sample1.lif','sample2.lif'])
df = lr.data_df
```
