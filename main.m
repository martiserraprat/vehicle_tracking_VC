%% Script Principal: Detecció de Cotxes
clear; clc; close all;

% Paràmetres Tasca 3
llindar = 62;

% Paràmetres Tasca 4
alpha = 1.5;
beta = 30;

% 1. Carregar dades
fprintf('Carregant imatges...\n');
mat = FuncionsPP.generarMatrius();

% Split Train/Test (MATLAB usa indexació des de 1)
train_mat = mat(:,:, 1:150);
test_mat = mat(:,:, 151:300);

% 2. Model de fons
[mitjana, desviacio] = FuncionsPP.calcularModelFons(train_mat);

% 3. Processar (Opcio 3 o 4)
opcio = 4;
fprintf('Generant resultats (Tasca %d)...\n', opcio);
res = FuncionsPP.generar_tots_resultats(opcio, test_mat, llindar, alpha, beta, mitjana, desviacio);

% 4. Guardar vídeo (Equivalent a utils.gravar_video)
v = VideoWriter('cotxes_detectats_MATLAB.avi');
v.FrameRate = 20;
open(v);
for i = 1:size(res, 3)
    % MATLAB necesita 3 canales o un mapa de colores para VideoWriter
    frame = res(:,:,i);
    writeVideo(v, repmat(frame, [1, 1, 3])); 
end
close(v);

% 5. Groundtruth i Accuracy
fprintf('Calculant Accuracy...\n');
gt_test = FuncionsPP.carregar_groundtruth_test();
[accuracy_mitjana, acc_per_img] = FuncionsPP.calcular_accuracy(res, gt_test);

% 6. Resultats
fprintf('Accuracy mitjana: %.4f\n', accuracy_mitjana);

% Plot (Equivalent a utils.print_plot_ACC)
figure;
plot(acc_per_img, 'LineWidth', 1.5);
title('Accuracy per frame');
xlabel('Frame');
ylabel('Accuracy');
grid on;