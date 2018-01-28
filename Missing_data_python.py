from sklearn.preprocessing import Imputer

# strategy pode ser 'mean', 'median' ou 'most_frequent'
# axis 0 para colunas e 1 para linhas
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
# entre colchetes os dois pontos indica que todas as linhas estão sendo selecionadas
# e o segundo parametro indica que somente a primeira e segunda colunas estao sendo selecionadas
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform([X[:, 1:3])
