import subprocess

def parse_line_segment(line):
    parts = line.split()
    if len(parts) != 9:
        return None
    segment_id = int(parts[1])
    x0 = float(parts[2])
    y0 = float(parts[3])
    x1 = float(parts[4])
    y1 = float(parts[5])
    beam_width = float(parts[6])
    color = int(parts[7], 16)
    flags = int(parts[8])

    # Extract RGBA components from the color
    a = (color >> 24) & 0xFF
    r = (color >> 16) & 0xFF
    g = (color >> 8) & 0xFF
    b = color & 0xFF

    return {
        "segment_id": segment_id,
        "x0": x0,
        "y0": y0,
        "x1": x1,
        "y1": y1,
        "beam_width": beam_width,
        "color": {
            "a": a,
            "r": r,
            "g": g,
            "b": b
        },
        "flags": flags
    }

def main():
    process = subprocess.Popen(["./mame"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    for line in process.stdout:
        line = line.strip()
        if line.startswith("S "):
            segment = parse_line_segment(line)
            if segment:
                print(f"Parsed Segment: {segment}")
        elif line == "E":
            print("End of Frame")

if __name__ == "__main__":
    main()
