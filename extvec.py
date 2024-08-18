import subprocess

def parse_point(line):
    parts = line.split()
    if len(parts) != 6:
        return None
    segment_id = int(parts[1])
    x = float(parts[2])
    y = float(parts[3])
    color = int(parts[4], 16)
    intensity = int(parts[5])

    # Extract RGB components from the color
    r = (color >> 16) & 0xFF
    g = (color >> 8) & 0xFF
    b = color & 0xFF

    return {
        "segment_id": segment_id,
        "x": x,
        "y": y,
        "color": {
            "r": r,
            "g": g,
            "b": b
        },
        "intensity": intensity
    }

def main():
    process = subprocess.Popen(["./mame"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    for line in process.stdout:
        line = line.strip()
        if line.startswith("P "):
            point = parse_point(line)
            if point:
                print(f"Parsed Point: {point}")
        elif line == "E":
            print("End of Frame")

if __name__ == "__main__":
    main()
