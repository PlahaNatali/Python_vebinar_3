text = "За день до начала раскопочного сезона в Мериде произошло восстание, в ходе которого был убит губернатор Карильо. Тем не менее силами археолога Эрла Морриса 18 мая раскопочный проект стартовал. Начинать пришлось с обустройства бывшей асьенды Эдварда Томпсона, разорённой пеонами в 1921 году. Была реставрирована и церковь Сан-Исидоро, сохранившаяся колокольня которой отмечала начало и конец утренних работ и сиесту (с шести до одиннадцати, и с часа дня до половины пятого). В ризнице оборудовали фотолабораторию, поставили бензиновый генератор и водяной насос. Специалисты жили в усадебном доме, рабочие — в двух каменных бараках под соломенной крышей. Постройки обсадили апельсиновыми деревьями, дававшими тень. Развлечения были однообразными: пластинки для граммофона содержали только классическую музыку (современные мелодии Морли считал недостойными «почтенности руин»)[Комм. 4], а игра в бридж казалась скучной. Жалованье выплачивалось каждые две недели; сумма расходов за один раз составляла 1500 серебряных песо, которые специально доставлялись из Мериды. Это тоже был важный ритуал и род развлечения. К 1932 году жалованье рабочим было увеличено вдвое. Число рабочих колебалось: в сезон 1925 года было нанято 69 человек, но затем найм продолжался, дойдя до 82 копачей. По мере роста профессионализма Морли сократил рабочую бригаду до 33 человек. С ними сложились практически семейные отношения: Морли стал крёстным более двадцати индейских детей. Талантливому сыну одного из рабочих Сильванус дал образование в Санта-Фе, и он стал одним из самых успешных гидов на руинах."

my_dict = {}
text_list = text.lower().split()
text_list_new = [''.join(filter(str.isalpha, a)) for a in text_list]  
while '' in text_list_new:
    text_list_new.remove('')
for word in text_list_new:
    my_dict.setdefault(word, text_list_new.count(word))
num_words = 1
while num_words <= 10:
    num_words += 1
    max_key = max(my_dict,  key=my_dict.get)
    print(f'{max_key:>5}  =  {my_dict[max_key]}')
    my_dict.pop(max_key)