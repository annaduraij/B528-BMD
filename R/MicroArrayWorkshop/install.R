if (!require("BiocManager",quietly = TRUE)) {
  install.packages("BiocManager")
}
BiocManager::install(version = "3.18")
BiocManager::install("limma")
BiocManager::install("GEOquery")
BiocManager::install("affy")
install.packages("pheatmap")