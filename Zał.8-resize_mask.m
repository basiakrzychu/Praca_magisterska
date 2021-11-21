dc = dir('D:\magisterka\masks\*.png');

for i = 1 : length(dc)
    filename = strcat('D:\magisterka\masks\',dc(i).name);
    name=erase(filename,'D:\magisterka\masks\');
    im = imread(filename);
    k=imresize(im,(1/7.5));
    imwrite(k,'D:\magisterka\scale_mask\'+string(name));
end


dc = dir('D:\magisterka\masks_2\*.png');

for i = 1 : length(dc)
    filename = strcat('D:\magisterka\masks_2\',dc(i).name);
    name=erase(filename,'D:\magisterka\masks_2\');
    im = imread(filename);
    k=imresize(im,(1/7.5));
    imwrite(k,'D:\magisterka\scale_masks_2\'+string(name));
end