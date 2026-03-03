classdef FuncionsPP
    methods (Static)
        function matfotos = generarMatrius()
            archivos = dir('img/*.jpg');
            num_fotos = length(archivos);
            
            % llegir primera img per saber el tamany
            primera_img = imread(fullfile(archivos(1).folder, archivos(1).name));
            if size(primera_img, 3) == 3
                primera_img = rgb2gray(primera_img);
            end
            [alto, ancho] = size(primera_img);
            
            % crear matriu (H x W x Num)
            matfotos = zeros(alto, ancho, num_fotos, 'uint8');
            
            for i = 1:num_fotos
                img = imread(fullfile(archivos(i).folder, archivos(i).name));
                if size(img, 3) == 3
                    img = rgb2gray(img);
                end
                matfotos(:,:,i) = img;
            end
        end

        function [mitjana, desviacio] = calcularModelFons(train_mat)
            train_double = double(train_mat);
            mitjana = mean(train_double, 3);
            desviacio = std(train_double, 0, 3);
        end

        function mascara = tasca_3(llindar, mitjana, img)
            resta = abs(double(img) - mitjana);
            mascara = resta > llindar; 
            mascara = uint8(mascara * 255); 
        end

        function mascara = tasca_4(alpha, beta, mitjana, desviacio, img)
            diff = abs(double(img) - mitjana);
            llindar_adaptatiu = alpha * desviacio + beta;
            mascara = uint8((diff > llindar_adaptatiu) * 255);
        end

        function res = generar_tots_resultats(opcio, test_mat, llindar, alpha, beta, mitjana, desviacio)
            [H, W, num_frames] = size(test_mat);
            res = zeros(H, W, num_frames, 'uint8');
            
            for i = 1:num_frames
                if opcio == 3
                    res(:,:,i) = FuncionsPP.tasca_3(llindar, mitjana, test_mat(:,:,i));
                else
                    res(:,:,i) = FuncionsPP.tasca_4(alpha, beta, mitjana, desviacio, test_mat(:,:,i));
                end
            end
        end

        function gt_mat = carregar_groundtruth_test()
            archivos = dir('groundtruth/*.png');
            count = 1;
            for i = 1:length(archivos)
                num = str2double(regexp(archivos(i).name, '\d+', 'match'));
                if num >= 1201 && num <= 1350
                    gt_files{count} = fullfile(archivos(i).folder, archivos(i).name);
                    count = count + 1;
                end
            end
            
            temp = imread(gt_files{1});
            [H, W] = size(temp);
            gt_mat = zeros(H, W, length(gt_files), 'uint8');
            
            for i = 1:length(gt_files)
                img = imread(gt_files{i});
                if size(img, 3) == 3, img = rgb2gray(img); end
                gt_mat(:,:,i) = img;
            end
        end

        function [accuracy_mitjana, acc_per_img] = calcular_accuracy(pred_seq, gt_seq)
            num_frames = size(pred_seq, 3);
            acc_per_img = zeros(num_frames, 1);
            
            for i = 1:num_frames
                pred_bin = pred_seq(:,:,i) == 255;
                gt_bin = gt_seq(:,:,i) == 255;
                
                acc_per_img(i) = sum(pred_bin(:) == gt_bin(:)) / numel(pred_bin);
            end
            accuracy_mitjana = mean(acc_per_img);
        end
    end
end