def bar(progress, root):
    import time
    progress['value'] = 20
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 40
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 50
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 60
    root.update_idletasks()
    time.sleep(1.5)

    progress['value'] = 80
    root.update_idletasks()
    time.sleep(1.5)
    progress['value'] = 100