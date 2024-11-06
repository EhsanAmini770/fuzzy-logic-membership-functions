import numpy as np
import matplotlib.pyplot as plt

distance = np.arange(-500, 501, 1)


def yakin(mesafe):
    if mesafe < 200:
        return 1
    elif 200 <= mesafe <= 500:
        return (500 - mesafe) / 300
    else:
        return 0

membership_values = np.array([yakin(m) for m in distance])

# yValues = []
# for i, v in enumerate(distance):
#     yValues.append(yakin(v))


plt.figure(figsize=(7, 4))
plt.plot(distance, membership_values, color='blue', label='YAKIN Bulanik Kümesi')
plt.xlabel('Mesafe')
plt.ylabel('Üyelik Değeri')
plt.title('YAKIN Bulanik Kümesi için Üyelik Fonksiyonu')
plt.axvline(x=200, color='green', linestyle='--', label='200')
plt.axvline(x=500, color='red', linestyle='--', label='500')
plt.legend()
plt.show()
