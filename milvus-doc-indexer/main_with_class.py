from src.services.milvus_service_class import MilvusService


if __name__ == "__main__":
  # Inicializar o serviço
  milvus = MilvusService()

  # Recriar a collection (isso vai apagar todos os dados existentes)
  milvus.recreate_collection()

  # Importar produtos dos arquivos markdown
  milvus.import_products_from_markdown("data/products")