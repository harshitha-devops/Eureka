# -*- coding: utf-8 -*-
# from odoo import http


# class EurekaDm(http.Controller):
#     @http.route('/eureka_dm/eureka_dm', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/eureka_dm/eureka_dm/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('eureka_dm.listing', {
#             'root': '/eureka_dm/eureka_dm',
#             'objects': http.request.env['eureka_dm.eureka_dm'].search([]),
#         })

#     @http.route('/eureka_dm/eureka_dm/objects/<model("eureka_dm.eureka_dm"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('eureka_dm.object', {
#             'object': obj
#         })
