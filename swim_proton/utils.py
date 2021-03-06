"""
Copyright 2019 EUROCONTROL
==========================================

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the
following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following
   disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following
   disclaimer in the documentation and/or other materials provided with the distribution.
3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products
   derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE
USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

==========================================

Editorial note: this license is an instance of the BSD license template as provided by the Open Source Initiative:
http://opensource.org/licenses/BSD-3-Clause

Details on EUROCONTROL: http://www.eurocontrol.int
"""
import logging
from typing import Optional
from proton import SSLDomain, SSLUnavailable


__author__ = "EUROCONTROL (SWIM)"


_logger = logging.getLogger(__name__)


def _get_ssl_domain(mode: int) -> Optional[SSLDomain]:
    """

    :param mode:
    :return:
    """
    try:
        return SSLDomain(mode)
    except SSLUnavailable as e:
        _logger.warning(str(e))
        return None


def create_ssl_domain(cert_db: str,
                      cert_file: Optional[str] = None,
                      cert_key: Optional[str] = None,
                      cert_password: Optional[str] = None,
                      mode: int = SSLDomain.VERIFY_PEER) -> Optional[SSLDomain]:
    """
    Creates an SSLDomain to be passed upon connecting to the broker

    :param cert_db: path to certificate DB
    :param cert_file: path to client certificate
    :param cert_key: path to client key
    :param cert_password: password of the client
    :param mode: one of MODE_CLIENT, MODE_SERVER, VERIFY_PEER, VERIFY_PEER_NAME, ANONYMOUS_PEER
    :return:
    """
    ssl_domain = _get_ssl_domain(mode)

    if ssl_domain is None:
        return None

    ssl_domain.set_trusted_ca_db(cert_db)

    if cert_file and cert_key and cert_password:
        ssl_domain.set_credentials(cert_file, cert_key, cert_password)

    return ssl_domain


def truncate_message(message: str, max_length: int) -> str:
    """

    :param message:
    :param max_length:
    :return:
    """
    return f"{message[:max_length]}..."
