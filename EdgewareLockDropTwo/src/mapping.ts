import {
  Locked as LockedEvent,
  Signaled as SignaledEvent
} from "../generated/Contract/Contract"
import { Locked, Signaled } from "../generated/schema"

export function handleLocked(event: LockedEvent): void {
  let entity = new Locked(
    event.transaction.hash.toHex() + "-" + event.logIndex.toString()
  )
  entity.owner = event.params.owner
  entity.eth = event.params.eth
  entity.lockAddr = event.params.lockAddr
  entity.term = event.params.term
  entity.edgewareAddr = event.params.edgewareAddr
  entity.isValidator = event.params.isValidator
  entity.time = event.params.time
  entity.save()
}

export function handleSignaled(event: SignaledEvent): void {
  let entity = new Signaled(
    event.transaction.hash.toHex() + "-" + event.logIndex.toString()
  )
  entity.contractAddr = event.params.contractAddr
  entity.edgewareAddr = event.params.edgewareAddr
  entity.time = event.params.time
  entity.save()
}
