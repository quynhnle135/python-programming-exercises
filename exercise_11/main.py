from hours_minutes_seconds import get_hours_minutes_seconds


def main():
    print(get_hours_minutes_seconds(60))
    print(get_hours_minutes_seconds(3600))
    print(get_hours_minutes_seconds(3556))
    print(get_hours_minutes_seconds(3660))


if __name__ == "__main__":
    main()