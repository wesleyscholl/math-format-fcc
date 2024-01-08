def add_time(start, duration, start_day=None):
  # Parsing start time
  start_hour, start_minute_period = start.split()[0].split(':')
  start_period = start.split()[1]
  start_hour = int(start_hour)
  start_minute = int(start_minute_period)

  # Parsing duration time
  duration_hours, duration_minutes = map(int, duration.split(':'))

  # Converting AM/PM to 24-hour format for start time
  if start_period == 'PM':
      start_hour += 12

  # Adding duration time to start time
  end_hour = start_hour + duration_hours
  end_minute = start_minute + duration_minutes

  # Handling extra hours if minutes exceed 60
  if end_minute >= 60:
      end_hour += 1
      end_minute -= 60

  # Calculating days and hours
  days_passed = end_hour // 24
  final_hour = end_hour % 24

  # Converting back to 12-hour format for final hour
  final_period = 'AM' if final_hour < 12 else 'PM'
  final_hour = final_hour if final_hour <= 12 else final_hour - 12
  final_hour = 12 if final_hour == 0 else final_hour

  # Forming the final result
  new_time = f"{final_hour}:{end_minute:02d} {final_period}"

  if start_day:
      # Calculate the new day of the week
      days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
      start_day_index = days_of_week.index(start_day.capitalize())
      new_day_index = (start_day_index + days_passed) % 7
      new_day = days_of_week[new_day_index]
      new_time += f", {new_day}"

  if days_passed == 1:
      new_time += " (next day)"
  elif days_passed > 1:
      new_time += f" ({days_passed} days later)"

  return new_time
