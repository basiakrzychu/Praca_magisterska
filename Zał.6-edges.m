gT=gTruth;

for i=1:length(gT.Droga)

if isempty(gTruth.Droga{i,1})==0
x=gT.Droga{i,1}{1, 1}(:,1);
y=gT.Droga{i,1}{1, 1}(:,2);
bw = poly2mask(x,y,1080,1920);
bw2=uint8(bw)+2;
bw2(bw2==3)=1;
bw3=bw2;

%for jakis
for xx=1:20
    for jj=2:height(bw2)-1
        for ii=2:length(bw2)-1
            if bw2(jj,ii)==2
                if bw2(jj,ii)~= bw2(jj,ii+1)
                bw3(jj,ii)=3;
                elseif bw2(jj,ii)~= bw2(jj+1,ii)
                bw3(jj,ii)=3;
                elseif bw2(jj,ii)~= bw2(jj,ii-1)
                bw3(jj,ii)=3;
                elseif bw2(jj,ii)~= bw2(jj-1,ii)
                bw3(jj,ii)=3;
                end
            end
            
        end
    end
    bw2=bw3;
end

plik=gT.imageFilename(i);
plik2=erase(plik,'D:\magisterka\color\');
plik3=erase(plik2,'.jpg');
imwrite(bw2,'D:\magisterka\masks_2\mask_'+string(plik3)+'.png');


end
end