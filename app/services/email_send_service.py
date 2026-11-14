import os
from html import escape
import resend

resend.api_key = os.environ["RESEND_API_KEY"]


def send_new_order_email(order):
    def safe(value):
        return escape(str(value if value is not None else "Not provided"))

    resend.Emails.send({
        "from": "HOV <order@updates.houseofvange.com>",
        "to": ["house.of.vange@gmail.com"],
        "subject": f"New order from {order.name or 'Unknown'}",
        "html": f"""
            <h1>New House of Vange order</h1>
            <p><strong>Name:</strong> {safe(order.name)}</p>
            <p><strong>Contact:</strong> {safe(order.contact)}</p>
            <p><strong>Ready to buy:</strong> {safe(order.the_time_to_buy_is_now)}</p>
            <p><strong>Desire:</strong> {safe(order.desire)}</p>
            <p><strong>Acknowledged pricing:</strong>
            {safe(order.understand_that_hov_cost_money)}</p>
        """,
    })

def send_new_guestbook_entry_email(entry):
    def safe(value):
        return escape(str(value if value is not None else "Not provided"))

    resend.Emails.send({
        "from": "HOV <order@updates.houseofvange.com>",
        "to": ["house.of.vange@gmail.com"],
        "subject": f"New Guestbook Entry from {entry.author or 'Unknown'}",
        "html": f"""
            <h1>New House of Vange Guestbook Entry</h1>
            <p><strong>Author:</strong> {safe(entry.author)}</p>
            <p><strong>Message:</strong> {safe(entry.message)}</p>
        """,
    })

def send_new_comment_email(comment, piece):
    def safe(value):
        return escape(str(value if value is not None else "Not provided"))

    resend.Emails.send({
        "from": "HOV <order@updates.houseofvange.com>",
        "to": ["house.of.vange@gmail.com"],
        "subject": f"New Comment on {piece.title} ({piece.piece_description}) from {comment.author or 'Unknown'}",
        "html": f"""
            <h1>New House of Vange Comment on {piece.title}</h1>
            <p><strong>Description:</strong> {safe(piece.piece_description)}</p>
            <p><strong>Author:</strong> {safe(comment.author)}</p>
            <p><strong>Message:</strong> {safe(comment.message)}</p>
        """,
    })