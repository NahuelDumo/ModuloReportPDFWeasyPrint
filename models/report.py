# models/report.py
from odoo import models, api
from weasyprint import HTML

class Report(models.AbstractModel):
    _inherit = 'ir.actions.report'  # Heredamos de la clase base de reportes

    @api.model
    def _run_wkhtmltopdf(self, report_name, docids, data=None):
        """
        Sobrescribimos la función que usa wkhtmltopdf y la reemplazamos con WeasyPrint.
        """
        # Obtener el contenido HTML del reporte usando el sistema de QWeb
        report = self.env['ir.actions.report']._get_report_from_name(report_name)
        html_content = report.render_qweb_pdf(docids)[0]

        # Usamos WeasyPrint para convertir el HTML a PDF
        pdf = HTML(string=html_content).write_pdf()

        # Devolvemos el PDF generado por WeasyPrint
        return pdf
