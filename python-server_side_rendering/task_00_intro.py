#!/usr/bin/python3
"""
Module for generating personalized invitations from a template.
"""
import os


def generate_invitations(template, attendees):
    """
    Generates personalized invitation files from a template and a list of attendees.
    """
    # 1. Məlumat tiplərinin yoxlanılması
    if not isinstance(template, str):
        print("Error: Template should be a string.")
        return
    
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees should be a list of dictionaries.")
        return

    # 2. Boş girişlərin (inputs) yoxlanılması
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # 3. İştirakçıların (attendees) işlənməsi
    for index, attendee in enumerate(attendees, start=1):
        content = template

        # Hər bir dəyişən üçün məlumatı yoxlayırıq, yoxdursa "N/A" qoyuruq
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            
            # Şablondakı dəyişənləri real məlumatlarla əvəzləyirik
            content = content.replace("{" + key + "}", str(value))

        # 4. Çıxış faylının yaradılması
        output_filename = "output_{}.txt".format(index)
        try:
            with open(output_filename, 'w', encoding='utf-8') as f:
                f.write(content)
        except Exception as e:
            print("Error writing to file {}: {}".format(output_filename, e))
