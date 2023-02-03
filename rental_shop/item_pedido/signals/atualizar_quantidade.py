from django.db.models.signals import post_save
from django.dispatch import receiver
from item_pedido.models import ItemPedido


@receiver(post_save, sender=Item.ItemPedido)
def calcular_qtd_restante(sender, instance, created, **kwargs):

    post_save.disconnect(calcular_qtd_restante, sender=sender)
    if created:
    
        inst_pedido = ItemPedido.objects.get(
            item=instance
        )
        inst_pedido.calcular_quantidade_restante()
        inst_pedido.save()

    post_save.connect(calcular_qtd_restante, sender=sender)