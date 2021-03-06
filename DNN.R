

# DNN example 

# Best activation method
models = h2o.deeplearning(x = 2:53,  
                          y = 54,
                          data = data.train.h2o, 
                          nfolds=5,
                          activation = c("TanhWithDropout", "RectifierWithDropout", "MaxoutWithDropout"),
                          override_with_best_model=TRUE,
                          input_dropout_ratio = 0.2,
                          hidden_dropout_ratios = c(0.5,0.5,0.5),
                          balance_classes = TRUE, 
                          hidden = list(c(30,15,10)),
                          epochs = 500)
models@model[[1]]

# "RectifierWithDropout"

# Model with 3 layers
models.3layers = h2o.deeplearning(x = 2:53,  
                                  y = 54,
                                  data = data.train.h2o, 
                                  nfolds=5,
                                  activation = "RectifierWithDropout",
                                  override_with_best_model=T,
                                  input_dropout_ratio = 0.2,
                                  hidden_dropout_ratios = c(0.5,0.5,0.5),
                                  balance_classes = TRUE, 
                                  hidden = list(c(30,15,10), c(5,5,5)),
                                  epochs = 500)

# Model with 2 layers
models.2layers = h2o.deeplearning(x = 2:53,  
                                  y = 54,
                                  data = data.train.h2o, 
                                  nfolds=5,
                                  activation = "RectifierWithDropout",
                                  override_with_best_model=TRUE,
                                  input_dropout_ratio = 0.2,
                                  hidden_dropout_ratios = c(0.5,0.5),
                                  balance_classes = TRUE, 
                                  hidden = list(c(15,10), c(5,5)),
                                  epochs = 500)

# Confusion Tables
cm.3layers <- as.table(models.3layers@model[[1]]@model$confusion[1:2,1:2])
cm.2layers <- as.table(models.2layers@model[[1]]@model$confusion[1:2,1:2])

# Confusion Matrices
confusionMatrix(cm.3layers,positive="1")
confusionMatrix(cm.2layers,positive="1")

# Best Model
best.model = models.3layers@model[[1]]
test.predict.all <- as.data.frame(h2o.predict(best.model,data.test.h2o))[,3]

