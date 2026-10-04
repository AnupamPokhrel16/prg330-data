"""Module 6: file input/output - raw open() reading and writing, no Pandas at all."""

DATA_PATH = "Air_Quality.csv"
SUMMARY_PATH = "file_io_summary.txt"


def peek_header_and_first_row(path=DATA_PATH):
    """Read just the header line and the first data line of the real CSV."""
    with open(path, "r") as file:
        header_line = file.readline()
        first_data_line = file.readline()
    return header_line.strip(), first_data_line.strip()


def compute_aqi_stats_from_csv(path=DATA_PATH, max_lines=2000, aqi_column_index=9):
    """Read up to max_lines real data rows and total/average the AQI column by hand."""
    line_count = 0
    total_aqi = 0.0
    with open(path, "r") as file:
        file.readline()  # skip header
        for line in file:
            if line_count >= max_lines:
                break
            fields = line.strip().split(",")
            total_aqi += float(fields[aqi_column_index])
            line_count += 1
    average_aqi = total_aqi / line_count if line_count else 0
    return line_count, total_aqi, average_aqi


def write_summary(path, line_count, total_aqi, average_aqi):
    """Write a short summary report, built entirely from numbers computed above."""
    with open(path, "w") as out_file:
        out_file.write("Air Quality Project -- File I/O Summary\n")
        out_file.write("========================================\n")
        out_file.write(f"Lines read directly from CSV: {line_count}\n")
        out_file.write(f"Total AQI of those rows: {round(total_aqi, 2)}\n")
        out_file.write(f"Average AQI of those rows: {round(average_aqi, 2)}\n")


def read_summary(path):
    """Read the summary file back, to prove it saved correctly."""
    with open(path, "r") as in_file:
        return in_file.read()


if __name__ == "__main__":
    header, first_row = peek_header_and_first_row()
    print("Header:", header)
    print("First row:", first_row)

    line_count, total_aqi, average_aqi = compute_aqi_stats_from_csv()
    print("Rows read:", line_count, " Average AQI:", round(average_aqi, 2))

    write_summary(SUMMARY_PATH, line_count, total_aqi, average_aqi)
    print()
    print(read_summary(SUMMARY_PATH))
