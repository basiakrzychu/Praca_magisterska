dc = dir('D:\magisterka\images\*.jpg');

for i = 1 : length(dc)
    filename = strcat('D:\magisterka\images\',dc(i).name);
    name=erase(filename,'D:\magisterka\images\');
    im = imread(filename);
    k=imresize(im,(1/7.5));
    imwrite(k,'D:\magisterka\scale_images\'+string(name));
end