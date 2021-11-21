gT=gTruth;

for i=1:length(gT.Droga)
if isempty(gTruth.Droga{i,1})==0
x=gT.Droga{i,1}{1, 1}(:,1);
y=gT.Droga{i,1}{1, 1}(:,2);
bw = poly2mask(x,y,1080,1920);
%imshow(bw);


plik=gT.imageFilename(i);
plik2=erase(plik,'D:\magisterka\color\');
copyfile(string(plik),'D:\magisterka\images')
plik3=erase(plik2,'.jpg');
imwrite(bw,'D:\magisterka\masks\mask_'+string(plik3)+'.png');

% imshow(bw)
% hold on
% plot(x,y,'b','LineWidth',20)
% hold off
% saveas(gcf,'D:\magisterka\masks_2\mask_'+string(plik3)+'.png');

% I1 = imread('C:\Users\basiakrzychu\Documents\Python Scripts\Magisterka\masks\mask_'+string(plik3)+'.png');
% I2 =imread('C:\Users\basiakrzychu\Documents\Python Scripts\Magisterka\images\'+string(plik2));
% 
% imshow(I1+I2);
% imwrite(I1+I2,'C:\Users\basiakrzychu\Documents\Python Scripts\Magisterka\val\val_'+string(plik2));
end
end