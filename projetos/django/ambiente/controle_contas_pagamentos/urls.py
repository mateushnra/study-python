from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('controle_contas_pagamentos/pagamento', views.pagamento, name='pagamento'),
    path('controle_contas_pagamentos/cad_pagamento', views.cad_pagamento, name='cad_pagamento'),
    path('controle_contas_pagamentos/upd_pagamento/<pk>', views.upd_pagamento, name='upd_pagamento'),
    path('controle_contas_pagamentos/del_pagamento/<int:pk>', views.del_pagamento, name='del_pagamento'),
]