---
layout: default
title: Машинное обучение
author: Ирина Князева
---


**Факультет свободных искусств и наук (Компьютерные науки и искуственный интеллект) · Осень 2020 · [Smolny College (CS program)](https://artesliberales.spbu.ru/en/education/bakalavariat/computer-science-and-artificial-intelligence)**

| Преподаватель | [Князева Ирина](https://artesliberales.spbu.ru/ru/faculty/personalii/knyazeva ) i.knyazeva at spbu.ru|
| Ассистент | Ольга Талалаева| 
| Занятия   | Понедельник 13:00 – 16:20,  MsTeams |
| Материалы   | [Google Class](https://classroom.google.com/c/MTU4NDk0MTQwMDg2), [Notebooks](https://github.com/iknyazeva/ML2020/tree/master/assignments) |


## Описание

Курс является вводным в машинное обучение. Рассматриваются базовые практики создания проектов. Отдельное внимание уделяется методам подготовки и визуализации данных. Мы сфокусируемся на использовании библиотеки  scikit-learn и языка Python при построении всех этапов проекта. Курс будет легче проходить при наличии базовых знаний математики и программирования на Python, но отсутствие таковых не является критичным, просто будет тяжелей🤔 🤯, но надеюсь финишируем довольные 😃 


## Структура и содержание занятий

**Обозначения**: 🖥 слайды, 📓 Jupyter notebook, 🎥 YouTube video. Слайды и видео чужие, но я выбрала лучшие. Тетрадки свои


<table>
<!-- =============================== HEADER ================================ -->
  <thead>
    <tr>
      <th>Неделя </th>
      <th align="left">Вид занятий</th>
      <th align="left">Тема</th>
      <th align="left">Материалы</th>
    </tr>
  </thead>
  <tbody>
<!-- =============================== WEEK 1 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="week01/01">① (07/09)</a></td>
      <td rowspan="2">Теория</td>
      <td><a href="week01/01-1">Введение в github</a></td>
      <td rowspan="2">
        <a href="https://amueller.github.io/COMS4995-s19/slides/aml-02-python-git-testing/">🖥️</a>
        <a href="https://youtu.be/EPVwnG-n4B0">🎥</a> 
        <a href="https://youtu.be/pHiMN_gy9mk">🎥</a> 
      </td>
    </tr>
    <tr><td><a href="week01/MlRoadMap_final_Mosina_/"> Тернистый путь в машинное обучение 😵</a></td></tr>
    <tr>
      <td rowspan="1">Практика</td>
      <td>Знакомство с colab</td>
      <td>
        <a href="https://colab.research.google.com/drive/1A696xnGuUNRVzMvT_sWwjrNO2jJjrCS9?usp=sharing">Типы данных в Python📓</a>
      </td>
    </tr>
<!-- =============================== WEEK 2 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="week02/02">② (14/09)</a></td>
      <td rowspan="2">Теория</td>
      <td><a href="week01/01-1">Визуализация данных</a></td>
      <td rowspan="2">
        <a href="https://amueller.github.io/COMS4995-s19/slides/aml-03-matplotlib/">🖥️</a>
        <a href="https://youtu.be/O2zXpQmij_c">🎥</a>
      </td>
    </tr>
    <tr><td><a href="week01/01-2">  Распределения и гистограммы</a></td></tr>
    <tr>
      <td rowspan="1">Практика</td>
      <td><a href="en/week01/01-3">matplotlib</a></td>
      <td>
        <a href="https://colab.research.google.com/drive/1v3nd-31ycQtHIOd34-Nop1wimPjVcd_X?usp=sharing">Визуализация в Python📓</a>
      </td>
    </tr>
    <!-- =============================== WEEK3 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="week03/01">③ (21/09)</a></td>
      <td rowspan="2">Теория</td>
      <td><a href="week03/02">Типы данных, особенности работы с ними  </a></td>
      <td rowspan="2">
        <a href="https://www.datacamp.com/">🎥</a>
      </td>
    </tr>
    <tr><td><a href="week03/03">  Категориальные и числовые данные, кодирование 😵</a></td></tr>
    <tr>
      <td rowspan="1">Практика</td>
      <td><a href="en/week03/04">Работа с таблицами Pandas</a></td>
      <td>
        <a href="https://colab.research.google.com/drive/1f1ELMr3Cnn-4vZ3BrizYs5yzbLv7zFdT?usp=sharing"> Пример работы с Pandas📓</a>
        <a href="https://colab.research.google.com/drive/1qouQItx6PYM1U6FAlMr5y2JGFucS5oNf?usp=sharing"> SpbBars📓</a>
      </td>
    </tr>
    <!-- =============================== WEEK 4 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="week04/01">④ (28/09)</a></td>
      <td rowspan="2">Теория</td>
      <td><a href="week04/02">Элементы теории обучения. Обучение с учителем</a></td>
      <td rowspan="2">
        <a href="https://amueller.github.io/COMS4995-s19/slides/aml-04-supervised-learning">🖥️</a> 
        <a href="https://www.youtube.com/playlist?list=PLLssT5z_DsK-h9vYZkQkYNWcItqhlRJLN">Плейлист от Anrew NG (2,3)🎥</a>
        <a href="https://youtu.be/MEEWqrJEtTg">В примерах от Andreas🎥</a>
        <a href="https://youtu.be/RflfnCsgNyI">Что такое обучение (hard)🎥</a>
      </td>
    </tr>
    <tr><td><a href="week04/03"> Повторяем линейную алгебру </a></td></tr>
    <tr>
      <td rowspan="1">Практика</td>
      <td><a href="en/week04/03"></a>Манипуляции с матрицами</td>
      <td>
        <a href="https://www.youtube.com/playlist?list=PLLssT5z_DsK-h9vYZkQkYNWcItqhlRJLN">Algebra review in Anrew NG (Ch 3)🎥</a>
        <a href="https://colab.research.google.com/drive/1JtZWAqEnoiGoC-yE-XsWGweJiwT0LdsP?usp=sharing"> Матрицы и вектора📓</a>
      </td>
    </tr>
    <!-- =============================== WEEK 5 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="week05/05">⑤ (05/10)</a></td>
      <td rowspan="2">Теория</td>
      <td><a href="week01/01-1">Линейные методы регрессии</a></td>
      <td rowspan="2">
        <a href="https://habr.com/ru/company/ods/blog/323890/">Статья на Хабре🖥️</a> <a href="https://youtu.be/3cZ_ScHonsI">Видео от A.Mueller🎥</a>
        <a href="https://www.youtube.com/playlist?list=PLLssT5z_DsK-h9vYZkQkYNWcItqhlRJLN">Регрессия от Anrew NG (Ch 2)🎥</a>
      </td>
    </tr>
    <tr><td><a href="week05/05"> Метод наименьших квадратов, вероятностный взгляд: правдоподобие</a></td></tr>
    <tr>
      <td rowspan="1">Практика</td>
      <td><a href="en/week01/01-3">Линейная регрессия в scikit-learn</a></td>
      <td>
TBA
      </td>
    </tr>
    <!-- =============================== WEEK 6 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="week06/06">⑥ (12/10)</a></td>
      <td rowspan="2">Теория</td>
      <td><a href="week06/06-1">Линейные методы классификации</a></td>
      <td rowspan="2">
       <a href="https://habr.com/ru/company/ods/blog/323890/">Статья на Хабре🖥️</a> <a href="https://youtu.be/MRfLSgJyfpQ">Видео от A.Mueller🎥</a>
        <a href="https://www.youtube.com/playlist?list=PLLssT5z_DsK-h9vYZkQkYNWcItqhlRJLN">Классификация от Anrew NG (Ch 2)🎥</a>
      </td>
    </tr>
    <tr><td><a href="week06/06-1">  SVM </a></td></tr>
    <tr>
      <td rowspan="1">Практика</td>
      <td><a href="en/week06/06-2">Примеры в scikit-learn</a></td>
      <td>
TBA
      </td>
    </tr>
    <!-- =============================== WEEK 7 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="week02/02">⑦  (19/10)</a></td>
      <td rowspan="2">Теория</td>
      <td><a href="week01/01-1">Решающие деревья, случайный лес</a></td>
      <td rowspan="2">
        <a href="https://www.vision.rwth-aachen.de/media/course/SS/2019/computer-vision/cv19-part02-image-processing.pdf">🖥️</a> <a href="https://youtu.be/hpqrDUuk7HY">🎥</a>
        <a href="https://youtu.be/5xdbJ7z4Nrc">🎥</a>
      </td>
    </tr>
    <tr><td><a href="week01/01-2"> Градиентный бустинг</a></td></tr>
    <tr>
      <td rowspan="1">Практика</td>
      <td><a href="en/week01/01-3">sklearn,  xgboost, catboost</a></td>
      <td>
TBA
      </td>
    </tr>
    <!-- =============================== WEEK 8 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="week02/02">⑧ (26/10)</a></td>
      <td rowspan="2">Теория</td>
      <td><a href="week01/01-1">Оценка моделей: метрики качества</a></td>
      <td rowspan="2">
        <a href="https://www.vision.rwth-aachen.de/media/course/SS/2019/computer-vision/cv19-part02-image-processing.pdf">🖥️</a> <a href="https://youtu.be/hpqrDUuk7HY">🎥</a>
        <a href="https://youtu.be/5xdbJ7z4Nrc">🎥</a>
      </td>
    </tr>
    <tr><td><a href="week01/01-2">  Кросс-валидация, настройка гиперпараметров </a></td></tr>
    <tr>
      <td rowspan="1">Практика</td>
      <td><a href="en/week01/01-3">Оценки моделей и кросс-валидация с sklearn</a></td>
      <td>
TBA
      </td>
    </tr>
    <!-- =============================== WEEK 9 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="week02/02">⑨ (2/11)</a></td>
      <td rowspan="2">Теория</td>
      <td><a href="week01/01-1">Интерпретация моделей</a></td>
      <td rowspan="2">
        <a href="https://www.vision.rwth-aachen.de/media/course/SS/2019/computer-vision/cv19-part02-image-processing.pdf">🖥️</a> <a href="https://youtu.be/hpqrDUuk7HY">🎥</a>
        <a href="https://youtu.be/5xdbJ7z4Nrc">🎥</a>
      </td>
    </tr>
    <tr><td><a href="week01/01-2">  Отбор признаков</a></td></tr>
    <tr>
      <td rowspan="1">Практика</td>
      <td><a href="en/week01/01-3">Средства для отбора признаков</a></td>
      <td>
TBA
      </td>
    </tr>
    <!-- =============================== WEEK 10 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="week02/02">⑩ (09/11)</a></td>
      <td rowspan="2">Теория</td>
      <td><a href="week01/01-1">Снижение размерности: основные методы</a></td>
      <td rowspan="2">
        <a href="https://www.vision.rwth-aachen.de/media/course/SS/2019/computer-vision/cv19-part02-image-processing.pdf">🖥️</a> <a href="https://youtu.be/hpqrDUuk7HY">🎥</a>
        <a href="https://youtu.be/5xdbJ7z4Nrc">🎥</a>
      </td>
    </tr>
    <tr><td><a href="week01/01-2">  Матричные разложения: SVD, PCA </a></td></tr>
    <tr>
      <td rowspan="1">Практика</td>
      <td><a href="en/week01/01-3">Средства sklearn снижения размерности</a></td>
      <td>
TBA
      </td>
    </tr>
     <!-- =============================== WEEK 11 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="week02/02">⑪ (16/11)</a></td>
      <td rowspan="2">Теория</td>
      <td><a href="week01/01-1">Кластеризация</a></td>
      <td rowspan="2">
        <a href="https://www.vision.rwth-aachen.de/media/course/SS/2019/computer-vision/cv19-part02-image-processing.pdf">🖥️</a> <a href="https://youtu.be/hpqrDUuk7HY">🎥</a>
        <a href="https://youtu.be/5xdbJ7z4Nrc">🎥</a>
      </td>
    </tr>
    <tr><td><a href="week01/01-2">  Модели смесей: вероятностный подход</a></td></tr>
    <tr>
      <td rowspan="1">Практика</td>
      <td><a href="en/week01/01-3">sklearn</a></td>
      <td>
TBA
      </td>
    </tr>
 <!-- =============================== WEEK 12 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="week02/02">⑫ (14/09)</a></td>
      <td rowspan="2">Теория</td>
      <td><a href="week01/01-1">Знакомство с нейронными сетями</a></td>
      <td rowspan="2">
        <a href="https://www.vision.rwth-aachen.de/media/course/SS/2019/computer-vision/cv19-part02-image-processing.pdf">🖥️</a> <a href="https://youtu.be/hpqrDUuk7HY">🎥</a>
        <a href="https://youtu.be/5xdbJ7z4Nrc">🎥</a>
      </td>
    </tr>
    <tr><td><a href="week01/01-2">  Градиентный спуск</a></td></tr>
    <tr>
      <td rowspan="1">Практика</td>
      <td><a href="en/week01/01-3">Персептрон в keras</a></td>
      <td>
TBA
      </td>
    </tr>
 <!-- =============================== WEEK 13 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="week02/02">⑬ (14/09)</a></td>
      <td rowspan="2">Теория</td>
      <td><a href="week01/01-1">Сверточные нейронные сети для работы с изображениями</a></td>
      <td rowspan="2">
        <a href="https://www.vision.rwth-aachen.de/media/course/SS/2019/computer-vision/cv19-part02-image-processing.pdf">🖥️</a> <a href="https://youtu.be/hpqrDUuk7HY">🎥</a>
        <a href="https://youtu.be/5xdbJ7z4Nrc">🎥</a>
      </td>
    </tr>
    <tr><td><a href="week01/01-2"> Рекурентные нейронные сети для работы с последовательностями</a></td></tr>
    <tr>
      <td rowspan="1">Практика</td>
      <td><a href="en/week01/01-3">примеры в Keras</a></td>
      <td>
TBA
      </td>
    </tr>
 <!-- =============================== WEEK 14 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="week02/02">⑭ (14/09)</a></td>
      <td rowspan="2">Теория</td>
      <td><a href="week01/01-1">Основные этапы построения проекта</a></td>
      <td rowspan="2">
        <a href="https://www.vision.rwth-aachen.de/media/course/SS/2019/computer-vision/cv19-part02-image-processing.pdf">🖥️</a> <a href="https://youtu.be/hpqrDUuk7HY">🎥</a>
        <a href="https://youtu.be/5xdbJ7z4Nrc">🎥</a>
      </td>
    </tr>
    <tr><td><a href="week01/01-2"> Data story telling</a></td></tr>
    <tr>
      <td rowspan="1">Практика</td>
      <td><a href="en/week01/01-3">Работа с пайплайнами</a></td>
      <td>
TBA
      </td>
    </tr>
  <!-- =============================== WEEK 14 ================================ -->
  <tr>
    <td rowspan="3" align="center">⑮ (14/09)</td><td rowspan="3" align="center">Презентация проектов  🎭</td><td rowspan="3" align="center">🧑‍🎓👩‍🎓</td><td rowspan="3" align="center">🏆</td>
  </tr>
  </tbody>
</table>

