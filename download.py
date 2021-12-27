import requests, os
folder = input('Enter Folder: ')
dir_path = os.path.join(os.getcwd(), folder)
try:
    os.mkdir(dir_path)
except Exception as err:
    print(err)
finally:

    begin = 1
    end = 20
    for i in range(begin, end + 1):
        url = f"http://d6.o2tv.org/How%20I%20Met%20Your%20Mother/Season%2003/How%20I%20Met%20Your%20Mother%20-%20S03E{0 if i < 10 else ''}{i}%20(O2TvSeries.Com).mp4"
        response = requests.get(url)
        if response.status_code == 200:
            with open(os.path.join(dir_path, f"How I Met Your Mother - S03E0{i}.mp4"), 'wb') as file:
                print(f'Downloading: How I Met Your Mother - S03E0{i}.mp4', )
                for packet in response.iter_content(chunk_size=1024):
                    file.write(packet)
        else:
            print('Problem Dey. No connect')


