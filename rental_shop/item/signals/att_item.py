from django.db.models.signals import post_save
from django.dispatch import receiver
import logging
from item.models import Item

@receiver(post_save, sender=Item)
def alterar_qts_itens(sender, instance, **kwargs):

    item = (Item.objects.get(id=instance.id))

    try:
        if item.quantidade > 0 and item.quantidade_pedida <= item.quantidade:
            item.quantidade_restante = item.quantidade
            item.quantidade_restante -= item.quantidade_pedida
            item.quantidade = item.quantidade_restante
            item.quantidade_pedida = 0
            Item.objects.filter(id=item.id).update(quantidade=item.quantidade_restante, quantidade_pedida=0, quantidade_restante=item.quantidade, disponivel = True)

        elif item.quantidade == 0:
            Item.objects.filter(id=item.id).update(disponivel = False)

        else:
            logging.exception("Quantidade solicidada maiorque a disponível!")
            
    except BaseException:
        logging.exception("Quantidade solicidada maiorque a disponível!")
